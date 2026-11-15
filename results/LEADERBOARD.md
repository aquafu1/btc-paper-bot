# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 7:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 429 windows, 11793 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 214 | 34.6 | 36.2 | $-174.42 | -8.2% | $825.58 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1005 | 50.6 | 50.0 | $-294.98 | -2.9% | $705.02 | -0.9 | done | can't tell from luck |
| value_ev10 | 553 | 39.2 | 40.3 | $-345.64 | -6.3% | $654.36 | -1.2 | done | can't tell from luck |
| trend_filter | 676 | 49.7 | 50.7 | $-412.51 | -6.1% | $587.49 | -1.6 | done | can't tell from luck |
| value_ev5 | 830 | 41.4 | 42.0 | $-431.13 | -5.2% | $568.87 | -1.3 | done | can't tell from luck |
| momentum_15m_0.10pct | 1193 | 49.2 | 50.0 | $-615.03 | -5.2% | $384.97 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1193 | 50.8 | 51.7 | $-707.88 | -5.9% | $292.12 | -2.2 | done | losing for real |
| coinflip | 1708 | 50.5 | 51.0 | $-783.01 | -4.6% | $216.99 | -1.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 1005 | 49.4 | 51.8 | $-898.23 | -8.9% | $101.77 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 1708 | 49.6 | 51.6 | $-1252.21 | -7.3% | $-252.21 | -3.1 | done | losing for real |
| always_up | 1708 | 46.3 | 50.6 | $-2071.77 | -12.1% | $-1071.77 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2669 | 47.6 | 49.4 | $-2049.54 |
| ETH | 2957 | 48.1 | 48.9 | $-1861.41 |
| SOL | 3061 | 47.8 | 49.4 | $-2386.41 |
| XRP | 3106 | 48.7 | 49.3 | $-1689.44 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
