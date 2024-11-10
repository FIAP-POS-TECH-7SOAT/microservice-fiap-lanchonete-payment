# microservice-fiap-lanchonete-payment

## Estrutura do Projeto

microservice-fiap-lanchonete-payment/
├── README.md
├── requirements.txt
├── server.py
├── src/
│ ├── config.py
│ ├── adapters/
│ │ ├── drivens/infra/
│ │ │ ├── providers/mercadopago_payment.py
│ │ │ └── settings.py
│ │ └── drivers/rest/payment_controller.py
│ ├── core/
│ │ ├── domain/models/payment_model.py
│ │ └── domain/application/
│ │ ├── services/payment_service.py
│ │ └── ports/providers/
│ │ ├── Ipayment_gateway.py
│ │ └── dtos/
│ │ ├── process_payment_request_dto.py
│ │ └── process_payment_response_dto.py
└── templates/
├── homepage.html
├── error.html
└── done.html
