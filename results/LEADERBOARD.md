# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 1:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1510 windows, 37562 settled trades, 394 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 764 | 34.6 | 35.4 | $-548.45 | -7.2% | $451.55 | -1.5 | done | can't tell from luck |
| value_ev10 | 1834 | 38.6 | 39.2 | $-933.19 | -5.1% | $66.81 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3737 | 50.9 | 50.1 | $-947.90 | -2.5% | $52.10 | -1.5 | done | can't tell from luck |
| value_ev5 | 2765 | 40.6 | 41.1 | $-1331.06 | -4.8% | $-331.06 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 3135 | 51.1 | 51.0 | $-1414.29 | -4.5% | $-414.29 | -2.6 | done | losing for real |
| momentum_60m_0.30pct | 3135 | 48.9 | 49.2 | $-1734.80 | -5.5% | $-734.80 | -3.1 | done | losing for real |
| trend_filter | 2225 | 48.5 | 50.3 | $-1926.80 | -8.7% | $-926.80 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3737 | 49.1 | 50.2 | $-2320.43 | -6.2% | $-1320.43 | -3.8 | done | losing for real |
| coinflip | 5410 | 50.0 | 50.0 | $-2380.52 | -4.4% | $-1380.52 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5410 | 50.2 | 51.3 | $-3330.25 | -6.2% | $-2330.25 | -4.7 | done | losing for real |
| always_up | 5410 | 48.0 | 49.2 | $-3587.24 | -6.6% | $-2587.24 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9752 | 48.0 | 48.7 | $-5392.60 |
| ETH | 10500 | 48.0 | 47.9 | $-5478.10 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
