import SwiftUI

struct HomeView: View {
    var body: some View {
        VStack(spacing: 30) {
            Text("StreamLive")
                .font(.largeTitle)
                .fontWeight(.bold)
            
            Spacer()
            
            NavigationLink(destination: Text("Streaming View - Coming Soon")) {
                Label("Start Stream", systemImage: "video.badge.plus")
                    .font(.headline)
                    .frame(maxWidth: .infinity)
                    .padding()
                    .background(Color.blue)
                    .foregroundColor(.white)
                    .cornerRadius(10)
            }
            
            NavigationLink(destination: Text("Viewer View - Coming Soon")) {
                Label("Find Stream", systemImage: "magnifyingglass")
                    .font(.headline)
                    .frame(maxWidth: .infinity)
                    .padding()
                    .background(Color.green)
                    .foregroundColor(.white)
                    .cornerRadius(10)
            }
            
            Spacer()
        }
        .padding()
    }
}

#Preview {
    NavigationStack {
        HomeView()
    }
}
