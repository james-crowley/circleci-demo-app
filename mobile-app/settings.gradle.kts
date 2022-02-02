pluginManagement {
    repositories {
        google()
        gradlePluginPortal()
        mavenCentral()
    }
    
}
rootProject.name = "kotlin-multiplatform-demo"

include(":androidApp")
include(":shared")

