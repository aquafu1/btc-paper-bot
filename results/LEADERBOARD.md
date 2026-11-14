# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 10:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 296 windows, 7868 settled trades, 69 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 780 | 53.6 | 51.9 | $-88.54 | -1.1% | $911.46 | -0.3 | done | can't tell from luck |
| value_ev20 | 147 | 35.4 | 36.4 | $-124.69 | -8.5% | $875.31 | -0.8 | Sun 2:15 AM | too few trades (147/200) |
| reversal_60m_0.30pct | 634 | 52.2 | 51.9 | $-243.99 | -3.8% | $756.01 | -1.0 | done | can't tell from luck |
| value_ev10 | 381 | 38.3 | 40.4 | $-361.07 | -9.5% | $638.93 | -1.6 | done | can't tell from luck |
| trend_filter | 425 | 46.6 | 50.2 | $-503.71 | -11.9% | $496.29 | -2.5 | done | losing for real |
| value_ev5 | 559 | 39.9 | 42.1 | $-539.93 | -9.7% | $460.07 | -2.0 | done | losing for real |
| momentum_60m_0.30pct | 634 | 47.8 | 49.7 | $-563.54 | -8.9% | $436.46 | -2.3 | done | losing for real |
| coinflip | 1176 | 50.3 | 50.9 | $-649.25 | -5.5% | $350.75 | -1.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 780 | 46.4 | 49.8 | $-857.88 | -11.0% | $142.12 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 1176 | 49.2 | 51.3 | $-965.84 | -8.2% | $34.16 | -2.9 | done | losing for real |
| always_up | 1176 | 47.1 | 50.3 | $-1237.78 | -10.5% | $-237.78 | -3.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1755 | 46.7 | 49.3 | $-1651.11 |
| ETH | 1968 | 47.3 | 48.7 | $-1754.95 |
| SOL | 2046 | 48.3 | 49.3 | $-1563.88 |
| XRP | 2099 | 48.6 | 49.0 | $-1166.27 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
