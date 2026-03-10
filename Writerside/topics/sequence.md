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
    
    browser.a -> gateway.a: request activate
    gateway.a -> gateway.a: verify user logged in
    break - user not present failure: {
        gateway.a -> browser.a: not logged in 
    }
    gateway.a -> central.a: request open lock
    
    authorize: {
        central.a -> auth.a: is authorized?
        break - unauthorized: {
            auth.a -> central.a: unauthorized
            central.a -> browser.a: unauthorized
        }
        auth.a -> central.a: authorized
    }

    attempt lock open: {
        central.a -> lock.a: activate
        lock.a -> central.a: reply
        central.a -> notification.a: prettied lock reply
        notification.a -> browser.a: prettied lock reply
    }
}
```
