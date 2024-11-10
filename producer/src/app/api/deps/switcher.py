from app.models.event_types import Topics, UserLogin, Registration


async def collect_user_login_payload(event, user: str, user_agent: str):
    return UserLogin(
            user_id=user,
            user_name=event.payload.get('user_name'),
            user_agent=user_agent
        )


async def collect_registration_payload(event, user, user_agent):
    return Registration(
            user_id=user,
            user_name=event.payload.get('user_name')
        )


switcher = {
    Topics.USER_LOGIN.value: collect_user_login_payload,
    Topics.REGISTRATION.value: collect_registration_payload
}
