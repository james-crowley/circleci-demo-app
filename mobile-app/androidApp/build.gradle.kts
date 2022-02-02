plugins {
    id("com.android.application")
    kotlin("android")
//    id("kotlin-android-extensions")
}

group = "com.circleci"
version = "1.0-SNAPSHOT"

dependencies {
    implementation(project(":shared"))
    implementation("com.google.android.material:material:1.4.0")
    implementation("androidx.appcompat:appcompat:1.3.1")
    implementation("androidx.constraintlayout:constraintlayout:2.1.1")
}

android {
    compileSdkVersion(31)
    buildToolsVersion = "30.0.2"
    defaultConfig {
        applicationId = "com.circleci.androidApp"
        minSdkVersion(24)
        targetSdkVersion(31)
        versionCode = 1
        versionName = "1.0"
    }
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_1_8
        targetCompatibility = JavaVersion.VERSION_1_8
    }
    buildTypes {
        getByName("release") {
            isMinifyEnabled = false
        }
    }
    buildFeatures {
        viewBinding = true
    }
}