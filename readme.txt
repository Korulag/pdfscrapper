Pre-requisites:
1. Database 'scrapper' is created in PostgreSQL manually.

Assumptions:
1. All links from PDF could be found in document annotations

Known issues:
Endpoints 'api/documents' and 'api/documents/$id/links' are failing with some
weird render recursion error.