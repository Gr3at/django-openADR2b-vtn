# Django OpenADR VTN

The project aims to provide a baseline, database ready, functional OpenADR VTN Server.
- There is no intend to provide implementation support for all endpoints defined in the specification. Feel free to contribute if you need something specific.
- A TDD approach is followed, as a result what you get should be sufficiently tested. A fact which could also help on setting up your custom VEN client app. 
- Currently working on support for OpenADR 2.0b (a rather old specification).
- Support for the new OpenADR 3.0 specification might be added later based on availability and interest. 
Leveraging Django's applications for separation of concerns and implementation logic for each openADR version is a no-brainer imo, so i intend to take full advantage of that.


## Roadmap

Gradually support should be added for several functionalities.
1. openADR 2.0b endpoints: EiRegisterParty, OadrPoll, oadrCreatedEvent and EiEvent
2. validation against openADR XML Schema Definition (XSD)

## Contributing

Just open an issue or/and a pull request if you want to add something.

