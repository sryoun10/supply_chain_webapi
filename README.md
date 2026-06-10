# supply_chain_webapi
This project provides a lightweight Flask API that models routing logic
for North American supply-chain paths. It exposes structured JSON endpoints
that can be used to simulate cross-border dataflow, compliance scenarios,
and control-validation workflows.

Built with Python and Flask to illustrate how simple, well-structured APIs
can support governance automation and evidence generation.

To access relevant countries for a particular supply chain route in North
America, please add '/' to the end of the url and then the three-letter
country code, such as PAN for Panama.

## File Structure
```
supply_chain_webapi/
├── app.py
├── index.html
└── README.md
```

## Future Enhancements
- Refactor country data into a dictionary or external JSON file
- Add query parameters (e.g. /route?to=PAN)
- Include error handling for invalid codes
- Add a simple frontend or Swagger UI for visualization
- Deploy to Render or Railway for live demo
