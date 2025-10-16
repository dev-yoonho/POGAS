import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect, TimeoutError as PlaywrightTimeoutError
from random_sleep import sleep_poisson


def find_opinion(playwright: Playwright, title: str):
    
    # 오류가 나면 최대 3회까지 다시 실행
    max_retries = 3
    for attempt in range(max_retries):
        browser = None
        context = None
        try:
            browser = playwright.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            
            page.goto("https://m.cafe.naver.com/ca-fe/home/search/discovery")
            page.wait_for_timeout(sleep_poisson()*1000)
            
            page.get_by_role("textbox", name="검색").click()
            page.get_by_role("textbox", name="검색").fill(title)
            page.keyboard.press("Enter")
            page.wait_for_timeout(sleep_poisson()*1000)
            
            page.locator(".SearchResultsListItemContainer").first.get_by_text(title).click()
            page.wait_for_timeout(sleep_poisson())
            # 게시글 내용
            content = page.locator("#postContent").inner_text()
            
            # 댓글 내용
            comments = []
            
            comment_locator = page.locator(".CommonComment > div")

            index = 0
            while True:
                current = comment_locator.nth(index)
                try:
                    text = current.inner_text(timeout=500).strip()
                except PlaywrightTimeoutError:
                    break  # 더 이상 매칭되는 요소가 없을 때 loop 종료

                if not text:
                    break  # 빈 문자열이면 종료
                comments.append(text)
                index += 1


            # ---------------------
            context.close()
            browser.close()
            return content, comments
            break
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(sleep_poisson())
                continue
            raise
        finally:
            if context is not None:
                context.close()
            if browser is not None:
                browser.close()
    
    



