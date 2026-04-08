import requests

AZDO_ORG = "your-org-name"

def validate_azdo_token(token):
    url = f"https://dev.azure.com/{AZDO_ORG}/_apis/projects?api-version=7.0"    #url to check token. need to search

    try:
        response = requests.get(
            url,
            headers={
                "Authorization": f"Bearer {token}"
            }
        )

        return response.status_code == 200

    except Exception:
        return False