# sequence
```D2
User Activates Mag-Lock: {
    shape: sequence_diagram
    browser: Web Browser
    gateway: API gateway
    central: Central Server
    auth: Auth Server
    lock: Mag-Lock
    notification: Notification Server
    
    browser -> gateway: request activate
    gateway -> central.a: forward request
    central.a -> central.a: user logged in
    break - user not present failure: {
        central.a -> gateway: not logged in
        gateway -> browser: not logged in 
    }
    
    authorize: {
        central.a -> auth.a: is authorized?
        break - unauthorized: {
            auth.a -> central.a: unauthorized
            central.a -> browser: unauthorized
        }
        auth.a -> central.a: authorized
    }

    attempt lock open: {
        central.a -> lock.a: activate
        lock.a -> central.a: reply
        central.a -> notification.a: prettied lock reply
        notification.a -> browser: prettied lock reply
    }
}
```
