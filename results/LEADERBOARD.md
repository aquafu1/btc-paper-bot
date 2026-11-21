# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 11:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1023 windows, 28487 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 526 | 34.8 | 35.1 | $-264.79 | -5.0% | $735.21 | -0.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2905 | 51.1 | 50.5 | $-871.95 | -3.0% | $128.05 | -1.6 | done | can't tell from luck |
| value_ev10 | 1306 | 37.6 | 39.2 | $-934.07 | -7.2% | $65.93 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2454 | 50.0 | 49.6 | $-1012.65 | -4.1% | $-12.65 | -2.0 | done | losing for real |
| trend_filter | 1704 | 49.8 | 50.8 | $-1171.06 | -6.9% | $-171.06 | -2.9 | done | losing for real |
| value_ev5 | 1981 | 39.5 | 41.0 | $-1373.61 | -6.9% | $-373.61 | -2.6 | done | losing for real |
| coinflip | 4084 | 50.5 | 50.4 | $-1640.34 | -4.0% | $-640.34 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2454 | 50.0 | 51.0 | $-1676.53 | -6.8% | $-676.53 | -3.5 | done | losing for real |
| momentum_15m_0.10pct | 2905 | 48.9 | 50.3 | $-1942.81 | -6.7% | $-942.81 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 4084 | 50.8 | 51.5 | $-2180.30 | -5.3% | $-1180.30 | -3.5 | done | losing for real |
| always_up | 4084 | 47.5 | 49.5 | $-3529.63 | -8.6% | $-2529.63 | -5.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6496 | 48.4 | 49.1 | $-3424.16 |
| ETH | 7076 | 48.1 | 48.5 | $-4404.70 |
| SOL | 7441 | 48.2 | 48.6 | $-4160.15 |
| XRP | 7474 | 48.2 | 48.4 | $-4608.76 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
