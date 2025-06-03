export default function UploadFile() {
    return (
        <div>
            <label className="block mb-2 text-sm font-medium text-gray-900" htmlFor="file-upload">Upload a file</label>
            <input className="block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50  focus:outline-none dark:border-gray-600 " type="file" id="file-upload" />
        </div>
    )
}