module default {
  type Person {
    required property username -> str;
    required property password_hash -> bytes;
    required property password_salt -> bytes;
  }

  type Item {
    required property name -> str;
    required property price -> str;
    required property categories -> str;

    property 
  }

  type Category {
  }

  type CustomerOrder {
    required property items;
    required property orderType;
  }

  type Payment {
    required property porder;
    required property paymentType;
    required property paidAmount;
  }
}
