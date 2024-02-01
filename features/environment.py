import os

DEV = "https://api.dev.hel.io/v1"
PROD = "https://api.hel.io/v1"


def before_feature(context, feature):
    # Environment settings.
    env_settings = os.getenv("ENVIRONMENT", "DEV")  # Default to DEV if not set
    if env_settings == "DEV":
        context.base_url = DEV
    else:
        context.base_url = PROD
    # Custom tags settings.
    if "not-implemented" in feature.tags:
        feature.skip()
        return


def before_scenario(context, scenario):
    if "not-implemented" in scenario.effective_tags:
        scenario.skip()
        return
