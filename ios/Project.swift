import ProjectDescription

let project = Project(
    name: "StreamLive",
    organizationName: "StreamLive",
    packages: [
        .package(url: "https://github.com/shogo4405/HaishinKit.swift", .upToNextMajor(from: "1.9.0")),
    ],
    targets: [
        .target(
            name: "StreamLive",
            destinations: .iOS,
            product: .app,
            bundleId: "com.streamlive.app",
            deploymentTargets: .iOS("17.0"),
            infoPlist: .extendingDefault(
                with: [
                    "UILaunchScreen": [
                        "UIColorName": "",
                        "UIImageName": "",
                    ],
                ]
            ),
            sources: ["Sources/**"],
            resources: ["Resources/**"],
            dependencies: [
                .package(product: "HaishinKit"),
            ]
        )
    ]
)
