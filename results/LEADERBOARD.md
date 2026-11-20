# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 11:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 877 windows, 24237 settled trades, 29 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 457 | 35.9 | 34.9 | $-59.37 | -1.3% | $940.63 | -0.2 | done | can't tell from luck |
| value_ev10 | 1110 | 38.6 | 39.1 | $-514.76 | -4.6% | $485.24 | -1.2 | done | can't tell from luck |
| momentum_60m_0.30pct | 2050 | 50.1 | 49.8 | $-809.16 | -3.9% | $190.84 | -1.8 | done | can't tell from luck |
| value_ev5 | 1677 | 40.1 | 41.0 | $-901.98 | -5.4% | $98.02 | -1.9 | done | can't tell from luck |
| trend_filter | 1429 | 50.2 | 51.0 | $-920.43 | -6.4% | $79.57 | -2.5 | done | losing for real |
| reversal_15m_0.10pct | 2476 | 50.5 | 50.4 | $-974.09 | -3.9% | $25.91 | -2.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 2476 | 49.5 | 50.4 | $-1390.86 | -5.6% | $-390.86 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 2050 | 49.9 | 50.9 | $-1429.39 | -7.0% | $-429.39 | -3.2 | done | losing for real |
| coinflip | 3504 | 50.1 | 50.3 | $-1581.02 | -4.5% | $-581.02 | -2.7 | done | losing for real |
| momentum_5m_0.00pct | 3504 | 51.3 | 51.7 | $-1584.04 | -4.5% | $-584.04 | -2.8 | done | losing for real |
| always_up | 3504 | 46.9 | 49.6 | $-3449.35 | -9.8% | $-2449.35 | -5.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5530 | 48.3 | 49.1 | $-3009.25 |
| ETH | 6030 | 48.2 | 48.5 | $-3690.26 |
| SOL | 6326 | 48.3 | 48.5 | $-3538.73 |
| XRP | 6351 | 48.4 | 48.5 | $-3376.22 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
