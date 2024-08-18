Issue Summary
Duration: 2024-08-18, 14:00 UTC to 15:30 UTC (1 hour 30 minutes)
Impact: The primary web service of our application experienced a significant slowdown, affecting approximately 70% of active users. Pages took up to 30 seconds to load, leading to a surge in support tickets and a noticeable drop in user engagement during the outage.
Root Cause: A memory leak in the caching layer led to resource exhaustion, causing the service to slow down as the cache servers started swapping memory to disk.
Timeline
14:00 UTC - Monitoring alert triggered, indicating high latency in web service response times.
14:05 UTC - Engineers noticed a spike in memory usage on the cache servers.
14:10 UTC - Initial investigation focused on database performance, assuming the issue might be related to slow queries.
14:25 UTC - Database queries were ruled out as the cause; attention shifted to the application servers.
14:35 UTC - Application servers were found to be healthy; cache layer became the new focus of investigation.
14:45 UTC - Cache servers were observed to be swapping memory heavily, leading to severe performance degradation.
14:50 UTC - The incident was escalated to the Site Reliability Engineering (SRE) team.
15:10 UTC - SRE team identified a memory leak in the caching software as the root cause.
15:20 UTC - Cache servers were restarted, and a temporary fix was applied to limit memory usage.
15:30 UTC - Full service was restored, and performance returned to normal levels.
Root Cause and Resolution
The root cause of the outage was a memory leak in the caching software, which led to unbounded memory growth over time. As memory usage increased, the operating system began swapping memory to disk, significantly slowing down the cache access times and, in turn, slowing down the overall web service.
The issue was resolved by restarting the cache servers to clear the memory and applying a temporary fix to cap the memory usage of the caching layer. A long-term fix will involve updating the caching software to a version that addresses the memory leak and conducting thorough testing before deploying it to production.
Corrective and Preventative Measures
Improvements:
Enhance monitoring of cache memory usage to detect leaks early.
Implement automated alerts for unusual memory growth patterns.
Perform regular load testing to identify potential performance bottlenecks.
Tasks:
Update Caching S
oftware: Patch the caching layer with the latest version to resolve the memory leak.
Monitor Memory Usage: Add detailed monitoring and alerts on memory usage for cache servers.
Test Caching Layer: Conduct stress tests on the caching layer to ensure it can handle peak loads without performance degradation.
Documentation: Update the incident response playbook to include steps for diagnosing and resolving cache-related issues.
This postmortem serves as a critical learning experience, highlighting the importance of thorough monitoring and proactive issue detection to minimize service disruptions in the future.

