# SQLAlchemy Core

This is a repository for basic practing with SQLAlchemy Core.

1. [CRUD](https://www.youtube.com/watch?v=CfZGWH_vNO0&ab_channel=SsaliJonathan)
2. [ORM](https://www.youtube.com/watch?v=XWtj4zLl_tg&ab_channel=SsaliJonathan)
3. [AsyncIO](https://www.youtube.com/watch?v=hkvngd_BUrY&ab_channel=SsaliJonathan)

## 📝 Learning notes

In session 3, I learn how to use SQLAlchemy Core with AsyncIO. `coroutine` is a function that can suspend its execution before reaching return, and it can resume from the same point later. It can be used to write asynchronous code in a synchronous style.

❓ QA: Why and how can we be able to close connection in SQLAlchemy Core in case we have been able to connect to our SQL Alchemy using AsyncIO?

We provide with a method that we call that is going to help us to close our connection after connecting to our database using SQLAlchemy and AsyncIO. That method is going to be the dispose method so if you want to access that dispose method what you shall have to do within a `coroutine` is to call the dispose method on the engine object.

```python
await engine.dispose()
```

if you set connect is false, you can use `async with` to close the connection automatically.

If you are interested SQLAlchemy, check my previous repository for [tutorial](https://github.com/yanliu1111/python-tutorial) practice.
