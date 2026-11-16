# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 9:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 487 windows, 13394 settled trades, 46 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 248 | 34.7 | 35.8 | $-159.21 | -6.4% | $840.79 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1139 | 51.1 | 49.8 | $-183.09 | -1.6% | $816.91 | -0.5 | done | can't tell from luck |
| value_ev10 | 632 | 38.8 | 40.1 | $-400.56 | -6.3% | $599.44 | -1.3 | done | can't tell from luck |
| momentum_15m_0.10pct | 1347 | 50.1 | 49.9 | $-429.94 | -3.2% | $570.06 | -1.2 | done | can't tell from luck |
| trend_filter | 787 | 49.4 | 50.7 | $-533.88 | -6.8% | $466.12 | -1.9 | done | can't tell from luck |
| value_ev5 | 932 | 40.8 | 41.8 | $-536.74 | -5.8% | $463.26 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 1347 | 49.9 | 51.5 | $-971.77 | -7.2% | $28.23 | -2.7 | done | losing for real |
| coinflip | 1941 | 49.9 | 50.8 | $-1042.41 | -5.4% | $-42.41 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1139 | 48.9 | 51.5 | $-1058.94 | -9.3% | $-58.94 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 1941 | 49.5 | 51.7 | $-1484.11 | -7.6% | $-484.11 | -3.5 | done | losing for real |
| always_up | 1941 | 46.4 | 50.4 | $-2266.57 | -11.7% | $-1266.57 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3020 | 47.3 | 49.3 | $-2456.07 |
| ETH | 3355 | 48.0 | 48.8 | $-2197.94 |
| SOL | 3487 | 47.8 | 49.3 | $-2478.93 |
| XRP | 3532 | 48.4 | 48.9 | $-1934.28 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
