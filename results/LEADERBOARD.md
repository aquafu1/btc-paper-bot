# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 11:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1311 windows, 34844 settled trades, 421 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 686 | 34.3 | 35.3 | $-520.82 | -7.6% | $479.18 | -1.5 | done | can't tell from luck |
| value_ev10 | 1679 | 38.8 | 39.2 | $-767.65 | -4.6% | $232.35 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3494 | 50.9 | 50.2 | $-1002.48 | -2.9% | $-2.48 | -1.7 | done | can't tell from luck |
| value_ev5 | 2535 | 40.5 | 41.1 | $-1251.76 | -4.9% | $-251.76 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2925 | 49.4 | 49.4 | $-1382.11 | -4.7% | $-382.11 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2925 | 50.6 | 51.0 | $-1576.45 | -5.4% | $-576.45 | -3.0 | done | losing for real |
| trend_filter | 2070 | 48.8 | 50.5 | $-1729.18 | -8.4% | $-729.18 | -3.9 | done | losing for real |
| momentum_15m_0.10pct | 3494 | 49.1 | 50.2 | $-2210.39 | -6.3% | $-1210.39 | -3.8 | done | losing for real |
| coinflip | 5012 | 49.9 | 50.1 | $-2286.18 | -4.6% | $-1286.18 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5012 | 50.3 | 51.4 | $-2935.71 | -5.9% | $-1935.71 | -4.3 | done | losing for real |
| always_up | 5012 | 47.9 | 49.3 | $-3624.35 | -7.2% | $-2624.35 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8439 | 47.9 | 48.8 | $-4968.71 |
| ETH | 9095 | 48.2 | 48.2 | $-4734.13 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
