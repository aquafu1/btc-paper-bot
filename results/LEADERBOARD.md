# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 6:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1338 windows, 35208 settled trades, 415 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 694 | 34.3 | 35.4 | $-528.07 | -7.6% | $471.93 | -1.5 | done | can't tell from luck |
| value_ev10 | 1697 | 38.7 | 39.2 | $-830.05 | -4.9% | $169.95 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3525 | 50.9 | 50.2 | $-979.25 | -2.8% | $20.75 | -1.6 | done | can't tell from luck |
| value_ev5 | 2561 | 40.4 | 41.1 | $-1333.07 | -5.2% | $-333.07 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2957 | 49.3 | 49.5 | $-1455.79 | -4.9% | $-455.79 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2957 | 50.7 | 50.9 | $-1525.83 | -5.2% | $-525.83 | -2.9 | done | losing for real |
| trend_filter | 2094 | 48.7 | 50.5 | $-1792.68 | -8.6% | $-792.68 | -4.0 | done | losing for real |
| momentum_15m_0.10pct | 3525 | 49.1 | 50.2 | $-2250.07 | -6.4% | $-1250.07 | -3.8 | done | losing for real |
| coinflip | 5066 | 49.9 | 50.1 | $-2346.55 | -4.6% | $-1346.55 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5066 | 50.3 | 51.4 | $-3030.92 | -6.0% | $-2030.92 | -4.4 | done | losing for real |
| always_up | 5066 | 47.9 | 49.3 | $-3648.92 | -7.2% | $-2648.92 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8614 | 47.8 | 48.9 | $-5243.36 |
| ETH | 9284 | 48.2 | 48.2 | $-4893.60 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
