import requests


def get_user_name():
    user_input = input("Enter your user name: ")
    return user_input


def get_user_activity(user_name):
    url = f"https://api.github.com/users/{user_name}/events"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def format_activity(events):
    if not events:
        print("No events found or unable to fetch events.")
        return

    # Dictionary to store push events grouped by repo
    push_commits = {}
    other_events = []

    for event in events:
        event_type = event.get("type")
        repo_name = event.get("repo", {}).get("name")

        if event_type == "PushEvent":
            # Count this as 1 commit
            if repo_name in push_commits:
                push_commits[repo_name] += 1
            else:
                push_commits[repo_name] = 1
        else:
            # Store non-push events for later processing
            other_events.append(event)

    formatted_output = []

    # Add grouped push events
    for repo_name, commit_count in push_commits.items():
        action = f"Pushed {commit_count} commit{'s' if commit_count > 1 else ''} to {repo_name}"
        formatted_output.append(f"- {action}")

    # Add other events
    for event in other_events[:10]:  # Limit to recent 10 non-push events
        event_type = event.get("type")
        repo_name = event.get("repo", {}).get("name")

        if event_type == "CreateEvent":
            ref_type = event.get("payload", {}).get("ref_type")
            if ref_type == "branch":
                ref_name = event.get("payload", {}).get("ref")
                action = f"Created branch '{ref_name}' in {repo_name}"
            elif ref_type == "repository":
                action = f"Created repository {repo_name}"
            else:
                action = f"Created a {ref_type} in {repo_name}"

        elif event_type == "DeleteEvent":
            ref_type = event.get("payload", {}).get("ref_type")
            ref_name = event.get("payload", {}).get("ref")
            action = f"Deleted {ref_type} '{ref_name}' from {repo_name}"

        elif event_type == "IssuesEvent":
            action_type = event.get("payload", {}).get("action")
            issue_number = event.get("payload", {}).get("issue", {}).get("number")
            action = f"{action_type.capitalize()} issue #{issue_number} in {repo_name}"

        elif event_type == "PullRequestEvent":
            action_type = event.get("payload", {}).get("action")
            pr_number = event.get("payload", {}).get("pull_request", {}).get("number")
            action = (
                f"{action_type.capitalize()} pull request #{pr_number} in {repo_name}"
            )

        elif event_type == "WatchEvent":
            action = f"Starred {repo_name}"

        elif event_type == "ForkEvent":
            forkee = event.get("payload", {}).get("forkee", {})
            fork_repo = forkee.get("full_name") if forkee else None
            if fork_repo:
                action = f"Forked {repo_name} to {fork_repo}"
            else:
                action = f"Forked {repo_name}"

        elif event_type == "IssuesCommentEvent":
            action_type = event.get("payload", {}).get("action")
            issue_number = event.get("payload", {}).get("issue", {}).get("number")
            action = f"{action_type.capitalize()} comment on issue #{issue_number} in {repo_name}"

        else:
            action = f"{event_type} in {repo_name}"

        formatted_output.append(f"- {action}")

    return formatted_output


def user_activity_tracker():
    user_name = get_user_name()
    user_activity = get_user_activity(user_name)

    if user_activity:
        activities = format_activity(user_activity)
        for activity in activities:
            print(activity)
    else:
        print(f"Unable to fetch events for user: {user_name}")


if __name__ == "__main__":
    user_activity_tracker()
