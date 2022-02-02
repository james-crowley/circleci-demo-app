## Kotlin Multiplatform Demo

This project demonstrates a simple CI/CD project for multiplatform applications. In this case, it will build Android and iOS apps.

Future enhancements may include additional platforms supported by [KMM](https://kotlinlang.org/docs/mpp-intro.html) such as Desktop, Web, etc.


## Setup

This project requires the Android SDK in order to build. (Installed separately)

There are several ways to indicate your SDK location for this build, but one simple option is to add a `local.properties` file to the project root that includes your Android SDK.

For example, this is a common installation directory for macOS:

```properties
sdk.dir=/Users/<username>/Library/Android/sdk
```

## Building the project

This command will build and package the application
```shell
./gradlew build
```

This command will run project checks such as linters and execute unit tests:
```shell
./gradlew check
```

This command will run project tests:
```shell
./gradlew allTests
```
