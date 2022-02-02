package com.circleci.shared


class Greeting {
    fun greeting(): String {
        return "Hello there, ${Platform().platform}!"
    }
}
