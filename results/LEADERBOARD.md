# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 12:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1554 windows, 38152 settled trades, 435 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 789 | 34.2 | 35.3 | $-623.30 | -7.9% | $376.70 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3780 | 50.9 | 50.0 | $-982.87 | -2.6% | $17.13 | -1.6 | done | can't tell from luck |
| value_ev10 | 1880 | 38.4 | 39.1 | $-1029.10 | -5.5% | $-29.10 | -1.9 | done | can't tell from luck |
| value_ev5 | 2826 | 40.4 | 41.0 | $-1442.75 | -5.1% | $-442.75 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 3175 | 50.9 | 50.9 | $-1536.77 | -4.8% | $-536.77 | -2.8 | done | losing for real |
| momentum_60m_0.30pct | 3175 | 49.1 | 49.2 | $-1644.18 | -5.2% | $-644.18 | -2.9 | done | losing for real |
| trend_filter | 2253 | 48.7 | 50.3 | $-1910.66 | -8.5% | $-910.66 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 3780 | 49.1 | 50.2 | $-2330.96 | -6.2% | $-1330.96 | -3.8 | done | losing for real |
| coinflip | 5498 | 50.0 | 49.9 | $-2379.06 | -4.3% | $-1379.06 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5498 | 50.2 | 51.3 | $-3383.04 | -6.2% | $-2383.04 | -4.7 | done | losing for real |
| always_up | 5498 | 48.2 | 49.2 | $-3534.50 | -6.4% | $-2534.50 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10032 | 47.9 | 48.7 | $-5737.80 |
| ETH | 10810 | 48.1 | 47.8 | $-5475.15 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
