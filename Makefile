include $(FAB_PATH)/common/mk/turnkey/lamp.mk
include $(FAB_PATH)/common/mk/turnkey.mk

COMMON_OVERLAYS += nodejs yarn
COMMON_CONF += nodejs-install apache-credit yarn
