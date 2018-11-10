# apiref

Internal API ref

# Submit compiled Blueprint

APIRef provides simple API to submit & update blueprint.
You can post blueprint via curl. Thus, it is easy to post it from ci environment.

```
$ curl -d "<html><h1>Hello!</h1></html>" \
       -H "APIRef-Token: w1Wvmpins1k3jUYAC142Ne3QabjYCBcrGESB2jJ1kj4" \
       http://localhost:8000/submit_compiled_blueprint/ -X POST
```
