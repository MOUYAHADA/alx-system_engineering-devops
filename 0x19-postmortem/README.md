# Postmortem: Website Slow Loading Due to Unoptimized Images

## Issue Summary
- **Duration of the Outage:** October 10, 2023, 10:00 AM - 10:45 AM (UTC)
- **Impact:** The website was very slow to load, affecting many users. About 75% of users experienced delays, with some pages taking over 10 seconds to load.
- **Root Cause:** The main reason for the slow loading was that images were not optimized. They did not have the `loading="lazy"` attribute, and they were not compressed, which made them too large.

## Timeline
- **10:00 AM:** The monitoring system detected slow page load times and sent an alert.
- **10:05 AM:** An engineer saw the alert and started checking the website's performance.
- **10:10 AM:** The engineer thought the server might be overloaded, so they checked CPU and memory usage, which were normal.
- **10:20 AM:** A customer complained about slow loading times, leading to a deeper investigation.
- **10:30 AM:** The team looked at the images on the website and found they were not optimized.
- **10:40 AM:** The issue was escalated to the web development team for quick action.
- **10:45 AM:** The problem was fixed by compressing images and adding `loading="lazy"` to all image tags.

## Root Cause and Resolution
The slow loading was caused by not optimizing images before the website was launched. The images were large and loaded all at once, which made the website slow. Without lazy loading, all images tried to load at the same time, using too much bandwidth and slowing down the page.

To fix the issue, we did the following:
1. Compressed all images using a tool to reduce their file sizes without losing quality.
2. Added the `loading="lazy"` attribute to all image tags, so images would only load when they were visible on the screen.
3. Reviewed all website images to ensure they were optimized.

## Corrective and Preventative Measures
To avoid this problem in the future, we suggest the following improvements and tasks:

### Improvements:
- Create a standard process for optimizing images before deploying the website.
- Regularly check website images to make sure they are optimized.

### TODO List:
1. **Use Image Optimization Tools:** Set up tools to automatically compress images before they are deployed.
2. **Add Lazy Loading Automatically:** Update website templates to include `loading="lazy"` for all images.
3. **Monitor Page Load Times:** Improve monitoring to track page load times and alert the team if they get too slow.
4. **Conduct Performance Checks:** Schedule regular checks of the website to find and fix slow areas.
5. **User Feedback System:** Create a way for users to report slow loading times directly, so we can respond quickly.

By making these changes, we can improve the website's performance and user experience, preventing similar issues in the future.

