# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 9:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 725 windows, 19951 settled trades, 51 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 381 | 33.3 | 34.9 | $-334.03 | -8.8% | $665.97 | -1.3 | done | can't tell from luck |
| reversal_15m_0.10pct | 2043 | 51.8 | 50.8 | $-406.15 | -2.0% | $593.85 | -0.9 | done | can't tell from luck |
| value_ev10 | 915 | 37.9 | 39.1 | $-622.90 | -6.8% | $377.10 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 1670 | 49.8 | 49.5 | $-652.73 | -3.9% | $347.27 | -1.6 | done | can't tell from luck |
| value_ev5 | 1382 | 40.6 | 41.1 | $-707.96 | -5.1% | $292.04 | -1.6 | done | can't tell from luck |
| trend_filter | 1171 | 49.9 | 50.9 | $-748.12 | -6.4% | $251.88 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 1670 | 50.2 | 51.2 | $-1110.85 | -6.7% | $-110.85 | -2.8 | done | losing for real |
| coinflip | 2892 | 50.2 | 50.3 | $-1211.30 | -4.2% | $-211.30 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 2043 | 48.2 | 50.0 | $-1533.92 | -7.5% | $-533.92 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 2892 | 50.9 | 51.8 | $-1542.09 | -5.3% | $-542.09 | -3.0 | done | losing for real |
| always_up | 2892 | 47.2 | 49.6 | $-2535.29 | -8.8% | $-1535.29 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4514 | 48.1 | 49.1 | $-2827.44 |
| ETH | 4970 | 48.1 | 48.5 | $-3061.03 |
| SOL | 5200 | 48.1 | 48.7 | $-3064.53 |
| XRP | 5267 | 48.6 | 48.4 | $-2452.33 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
