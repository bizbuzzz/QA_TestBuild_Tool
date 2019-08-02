fastlane_version '2.53.1'

before_all do
  #ensure_git_branch
  #ensure_git_status_clean
  #git_pull
	ENV["SLACK_URL"] ="https://hooks.slack.com/services/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"
end

platform :ios do
	private_lane :build do
		gym(
				scheme: "BBMobile",
				workspace: "./ios/BBMobile.xcworkspace",
				export_method: "ad-hoc",
				output_directory: "./build",
				clean: true,
				)
		slack_upload(
				slack_api_token: "xoxp-500863336260-594357945633-713463512598-467d7dc54dcbc648911a43999493baf2",
        title: "New version is available ",
        channel: "#mobileappbuild",
        file_path: "./build/*.ipa",
        initial_comment: "New Build is here"
				)
	end
end

platform :android do

 	private_lane :build do
		gradle(task: 'clean', project_dir: 'android/')
		gradle(task: 'assemble', build_type: 'Release', project_dir: 'android/')
		slack_upload(
          slack_api_token: "xoxp-500863336260-594357945633-713463512598-467d7dc54dcbc648911a43999493baf2",
          title: "New version is available ",
          channel: "#mobileappbuild",
          file_path: "./app/build/outputs/apk/release/app-release-unsigned.apk",
          initial_comment: "New Build is here"
					)
					
		private_lane :beta do
		gradle(task: 'clean', project_dir: 'android/')
		gradle(task: 'assemble', build_type: 'Debug', project_dir: 'android/')
		slack_upload(
          slack_api_token: "xoxp-500863336260-594357945633-713463512598-467d7dc54dcbc648911a43999493baf2",
          title: "New version is available ",
          channel: "#mobileappbuild",
          file_path: "./app/build/outputs/apk/debug/app-debug.apk",
          initial_comment: "New Build is here"
					)
	
	end

end

after_all do |lane|
    slack(
      message:"Successful build app"
    )

  #/app/build/outputs/apk/release/app-release-unsigned.apk
  #
  #
  end

  error do |lane,exception|
    slack(
      message:exception.message,
      success: false
    )
  end
