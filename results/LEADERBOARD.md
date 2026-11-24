# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 2:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1320 windows, 34977 settled trades, 429 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 687 | 34.2 | 35.3 | $-530.82 | -7.7% | $469.18 | -1.5 | done | can't tell from luck |
| value_ev10 | 1687 | 38.8 | 39.2 | $-802.80 | -4.8% | $197.20 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3504 | 50.8 | 50.2 | $-1046.82 | -3.0% | $-46.82 | -1.8 | done | can't tell from luck |
| value_ev5 | 2545 | 40.5 | 41.1 | $-1280.73 | -5.0% | $-280.73 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2939 | 49.4 | 49.4 | $-1403.98 | -4.8% | $-403.98 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2939 | 50.6 | 50.9 | $-1574.14 | -5.4% | $-574.14 | -3.0 | done | losing for real |
| trend_filter | 2082 | 48.8 | 50.5 | $-1770.23 | -8.5% | $-770.23 | -4.0 | done | losing for real |
| momentum_15m_0.10pct | 3504 | 49.2 | 50.2 | $-2185.31 | -6.2% | $-1185.31 | -3.7 | done | losing for real |
| coinflip | 5030 | 49.9 | 50.0 | $-2344.35 | -4.7% | $-1344.35 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5030 | 50.3 | 51.4 | $-2980.18 | -5.9% | $-1980.18 | -4.3 | done | losing for real |
| always_up | 5030 | 47.8 | 49.3 | $-3696.97 | -7.3% | $-2696.97 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8503 | 47.9 | 48.8 | $-5131.20 |
| ETH | 9164 | 48.2 | 48.2 | $-4900.89 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
