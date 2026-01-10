import ProjectDescription

let project = Project(
    name: "StreamLive",
    organizationName: "StreamLive",
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
            dependencies: []
        )
    ]
)
