# supply_chain_webapi
This is a basic web API for accessing country codes relevant to various supply chain routes throughout North America.

This project was developed using Python and incorporating flask, a lightweight web framework built on top of the Python language.

To access relevant countries for a particular supply chain route in North America, please add '/' to the end of the url and then the three-letter country code, such as PAN for Panama.

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
