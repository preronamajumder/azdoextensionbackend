import requests

AZDO_ORG = "preronamajumder"

def check_org_access(token):
    url = f"https://dev.azure.com/{AZDO_ORG}/_apis/projects?api-version=7.0"    #url to check token. need to search

    try:
        response = requests.get(
            url,
            headers={
                "Authorization": f"Bearer {token}"
            }
        )

        return response.status_code == 200

    except Exception as e:
        print("Error: ", e)
        return False
    
    
def validate_azdo_token(token):
    url = "https://app.vssps.visualstudio.com/_apis/profile/profiles/me?api-version=7.0"

    try:
        response = requests.get(
            url,
            headers={"Authorization": f"Bearer {token}"}
        )

        return response.status_code == 200

    except Exception as e:
        print("Error:", e)
        return False