from enum import StrEnum


class OrderStatus(StrEnum):
    PENDING = "pending"
    CONFIRME = "confirmed"
    PREPARING = "preparing"
    READY = "ready"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class PaymentMethod(StrEnum):
    CASH = "cash"
    CARD = "card"
    BANK_TRANSFER = "bank_transfer"
    MOBILE_MONEY = "mobile_money"
    

class PaymentStatus(StrEnum):
    SUCCESSFUL = "succesful"
    FAILED = "failed"
    REFUNDED = "refunded"
    AWAITING = "awaiting"


class DeliveryStatus(StrEnum):
    PENDING = "pending"
    ASSIGNED = "assigned"
    PICKED_UP = "picked_up"
    IN_TRANSIT = "in_transit"
    DELIVERED = "delivered"
    FAILED = "failed"
    CANCELLED = "cancelled"
