#include "MyApp.h"
#include "Student.h"
#define FMT_HEADER_ONLY
#include <fmt/core.h>

#define WINDOW_WIDTH  1920
#define WINDOW_HEIGHT 1080

MyApp::MyApp() {
    app_ = App::Create();
    window_ = Window::Create(app_->main_monitor(), WINDOW_WIDTH, WINDOW_HEIGHT, false, kWindowFlags_Titled | kWindowFlags_Resizable);
    overlay_ = Overlay::Create(window_, 1, 1, 0, 0);
    OnResize(window_.get(), window_->width(), window_->height());
    overlay_->view()->LoadURL("file:///index.html");
    app_->set_listener(this);
    window_->set_listener(this);
    overlay_->view()->set_load_listener(this);
    overlay_->view()->set_view_listener(this);
}

MyApp::~MyApp() {}

void MyApp::Run() {
    app_->Run();
}

void MyApp::OnUpdate() {
    /// This is called repeatedly from the application's update loop.
    /// You should update any app logic here.
}

void MyApp::OnClose(ultralight::Window* window) {
    app_->Quit();
}

void MyApp::OnResize(ultralight::Window* window, uint32_t width, uint32_t height) {
    /// This is called whenever the window changes size (values in pixels).
    /// We resize our overlay here to take up the entire window.
    overlay_->Resize(width, height);
}

void MyApp::OnFinishLoading(ultralight::View* caller, uint64_t frame_id, bool is_main_frame, const String& url) {
    /// This is called when a frame finishes loading on the page.
}

// JSValueRef ButtonClick(JSContextRef ctx, JSObjectRef function, JSObjectRef thisObject, size_t argumentCount, const JSValueRef arguments[], JSValueRef* exception) {

//     // Reading Content From CSV file
//     std::vector<std::vector<std::string>> content = ReadCSV("./assets/test.csv");

//     // Creating a JS Script to Display CSV Content when pressed
//     std::string jsScript = 
//     "var tag = document.createElement('p')\nvar text = '";
//     for(std::vector<std::string> row : content) {
//         for(std::string word : row)
//             jsScript += word + " ";
//         jsScript += "<br/>";
//     }

//     jsScript += 
//     "'\ntag.innerHTML = text\nvar element = document.getElementById('result')\nelement.appendChild(tag)\n";

//     JSStringRef script = JSStringCreateWithUTF8CString(jsScript.c_str());
//     // Execute it with JSEvaluateScript, ignoring other parameters for now
//     JSEvaluateScript(ctx, script, 0, 0, 0, 0);
//     // Release our string (we only Release what we Create)
//     JSStringRelease(script);
//     return JSValueMakeNull(ctx);
// }

// temp
std::string StudentTableScript(std::string container, std::string csvPath) {
    std::string JScript = ReadAll("./assets/CJavaScript/StudentTable.js");
    std::cout << JScript << std::endl;

    std::string HTMLTemplate = ReadAll("./assets/CHTML/StudentTableRow.html");
    std::string content = "";

    std::vector<std::vector<std::string>> csv = ReadCSV(csvPath);
    for(std::vector<std::string> row : csv) {
        std::string name = row[2], mclass = row[3], id = row[1];
        std::string HTML = HTMLTemplate;
        HTML = fmt::format(HTML.c_str(), fmt::arg("NAME", name.c_str()), fmt::arg("CLASS", mclass.c_str()), fmt::arg("ID", id.c_str()));
        content += HTML;
    }

    JScript = fmt::format(JScript.c_str(), fmt::arg("CONTAINER", container), fmt::arg("CONTENT", content.c_str()));
    return JScript;
}
// temp


void MyApp::OnDOMReady(ultralight::View* caller, uint64_t frame_id, bool is_main_frame, const String& url) {
    auto list = Student::LoadFromCSV("./assets/21TCLC_Nhat1.csv");
    for(Student s : list) {
        std::cout << s.GetName() << " " << s.GetClass() << " " << s.GetId() << std::endl;
    }
    std::string script = StudentTableScript("mainTable", "./assets/21TCLC_Nhat1.csv");
    // std::cout << script << std::endl;

    caller->EvaluateScript(script.c_str());
    // Acquire the JS execution context for the current page.
    // This call will lock the execution context for the current thread as long as the Ref<> is alive.
    // RefPtr<JSContext> context = caller->LockJSContext();
    // // Get the underlying JSContextRef for use with the
    // // JavaScriptCore C API.
    // JSContextRef ctx = context.get() -> ctx();
    // // Create a JavaScript String containing the name of our callback.
    // JSStringRef name = JSStringCreateWithUTF8CString("ButtonClick");
    // // Create a garbage-collected JavaScript function that is bound to our native C callback 'OnButtonClick()'.
    // // JSObjectRef func = JSObjectMakeFunctionWithCallback(ctx, name, ButtonClick);
    // // Get the global JavaScript object (aka 'window')
    // // JSObjectRef globalObj = JSContextGetGlobalObject(ctx);
    // // Store our function in the page's global JavaScript object so that it accessible from the page as 'OnButtonClick()'.
    // JSObjectSetProperty(ctx, globalObj, name, func, 0, 0);
    // // Release the JavaScript String we created earlier.
    // JSStringRelease(name);
}

void MyApp::OnChangeCursor(ultralight::View* caller, Cursor cursor) {
    /// This is called whenever the page requests to change the cursor.
    /// We update the main window's cursor here.
    window_->SetCursor(cursor);
}

void MyApp::OnChangeTitle(ultralight::View* caller, const String& title) {
    /// This is called whenever the page requests to change the title.
    /// We update the main window's title here.
    window_->SetTitle(title.utf8().data());
}