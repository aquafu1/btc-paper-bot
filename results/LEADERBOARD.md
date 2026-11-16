# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 4:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 561 windows, 15543 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1320 | 51.3 | 49.7 | $-242.45 | -1.8% | $757.55 | -0.7 | done | can't tell from luck |
| value_ev20 | 306 | 33.0 | 35.2 | $-355.92 | -11.6% | $644.08 | -1.6 | done | can't tell from luck |
| trend_filter | 899 | 50.5 | 51.1 | $-504.99 | -5.6% | $495.01 | -1.7 | done | can't tell from luck |
| value_ev10 | 737 | 37.3 | 39.4 | $-722.57 | -9.8% | $277.43 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 1578 | 49.6 | 49.8 | $-779.74 | -4.9% | $220.26 | -2.0 | done | can't tell from luck |
| value_ev5 | 1097 | 39.6 | 41.2 | $-907.69 | -8.3% | $92.31 | -2.4 | done | losing for real |
| reversal_15m_0.10pct | 1578 | 50.4 | 51.1 | $-982.94 | -6.2% | $17.06 | -2.5 | done | losing for real |
| coinflip | 2236 | 49.9 | 50.5 | $-1242.43 | -5.6% | $-242.43 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 1320 | 48.7 | 51.2 | $-1303.75 | -9.9% | $-303.75 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2236 | 50.3 | 51.9 | $-1551.04 | -6.9% | $-551.04 | -3.4 | done | losing for real |
| always_up | 2236 | 47.2 | 49.9 | $-2228.62 | -10.0% | $-1228.62 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3514 | 47.6 | 49.2 | $-2741.77 |
| ETH | 3872 | 47.9 | 48.6 | $-2762.07 |
| SOL | 4058 | 47.8 | 48.7 | $-3052.56 |
| XRP | 4099 | 48.6 | 48.6 | $-2265.73 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
