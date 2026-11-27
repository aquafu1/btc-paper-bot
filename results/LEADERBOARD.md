# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 12:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1552 windows, 38130 settled trades, 411 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 788 | 34.3 | 35.3 | $-613.30 | -7.8% | $386.70 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3780 | 50.9 | 50.0 | $-982.87 | -2.6% | $17.13 | -1.6 | done | can't tell from luck |
| value_ev10 | 1879 | 38.4 | 39.1 | $-1019.10 | -5.4% | $-19.10 | -1.9 | done | can't tell from luck |
| value_ev5 | 2824 | 40.5 | 41.0 | $-1422.75 | -5.0% | $-422.75 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 3172 | 51.0 | 50.9 | $-1506.77 | -4.8% | $-506.77 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 3172 | 49.0 | 49.2 | $-1667.89 | -5.3% | $-667.89 | -2.9 | done | losing for real |
| trend_filter | 2250 | 48.6 | 50.3 | $-1934.37 | -8.6% | $-934.37 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3780 | 49.1 | 50.2 | $-2330.96 | -6.2% | $-1330.96 | -3.8 | done | losing for real |
| coinflip | 5495 | 49.9 | 49.9 | $-2402.76 | -4.4% | $-1402.76 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5495 | 50.2 | 51.3 | $-3406.74 | -6.2% | $-2406.74 | -4.7 | done | losing for real |
| always_up | 5495 | 48.2 | 49.2 | $-3558.21 | -6.5% | $-2558.21 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10017 | 47.9 | 48.7 | $-5756.83 |
| ETH | 10803 | 48.1 | 47.8 | $-5504.65 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
