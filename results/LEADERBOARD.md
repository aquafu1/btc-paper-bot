# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 9:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1350 windows, 35381 settled trades, 410 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 699 | 34.2 | 35.4 | $-551.96 | -7.9% | $448.04 | -1.6 | done | can't tell from luck |
| value_ev10 | 1708 | 38.7 | 39.2 | $-837.95 | -4.9% | $162.05 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3538 | 50.8 | 50.1 | $-1043.33 | -2.9% | $-43.33 | -1.8 | done | can't tell from luck |
| value_ev5 | 2578 | 40.4 | 41.1 | $-1338.47 | -5.2% | $-338.47 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2973 | 49.4 | 49.5 | $-1455.27 | -4.9% | $-455.27 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2973 | 50.6 | 50.9 | $-1567.49 | -5.3% | $-567.49 | -2.9 | done | losing for real |
| trend_filter | 2104 | 48.7 | 50.5 | $-1809.16 | -8.6% | $-809.16 | -4.0 | done | losing for real |
| momentum_15m_0.10pct | 3538 | 49.2 | 50.3 | $-2209.90 | -6.2% | $-1209.90 | -3.8 | done | losing for real |
| coinflip | 5090 | 49.9 | 50.0 | $-2319.89 | -4.6% | $-1319.89 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5090 | 50.3 | 51.3 | $-3023.39 | -5.9% | $-2023.39 | -4.4 | done | losing for real |
| always_up | 5090 | 47.9 | 49.3 | $-3684.82 | -7.2% | $-2684.82 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8694 | 47.8 | 48.8 | $-5296.69 |
| ETH | 9377 | 48.2 | 48.2 | $-4960.73 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
