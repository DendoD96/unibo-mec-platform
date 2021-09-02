from typing import List
"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""
def check_OauthSecurity(token):
    return {'scopes': ['read:pets', 'write:pets'], 'uid': 'test_value'}

def validate_scope_OauthSecurity(required_scopes, token_scopes):
    return set(required_scopes).issubset(set(token_scopes))