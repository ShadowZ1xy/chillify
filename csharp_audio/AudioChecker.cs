using CSCore.CoreAudioAPI;

namespace CheckAudioStatus
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            System.Console.Write(AudioPlayingPeekValue(GetDefaultRenderDevice()));
        }

        public static MMDevice GetDefaultRenderDevice()
        {
            using (var enumerator = new MMDeviceEnumerator())
            {
                return enumerator.GetDefaultAudioEndpoint(DataFlow.Render, Role.Console);
            }
        }

        public static float AudioPlayingPeekValue(MMDevice device)
        {
            using (var meter = AudioMeterInformation.FromDevice(device))
            {
                return meter.PeakValue;
            }
        }
    }
}