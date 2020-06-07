include $(FAB_PATH)/common/mk/turnkey/lamp.mk
include $(FAB_PATH)/common/mk/turnkey.mk

COMMON_OVERLAYS += nodejs
COMMON_CONF += nodejs-install apache-credit
