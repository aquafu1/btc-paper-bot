# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 2:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 554 windows, 15359 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1307 | 51.3 | 49.7 | $-228.15 | -1.7% | $771.85 | -0.6 | done | can't tell from luck |
| value_ev20 | 302 | 33.4 | 35.2 | $-315.92 | -10.5% | $684.08 | -1.4 | done | can't tell from luck |
| trend_filter | 891 | 50.5 | 51.0 | $-489.63 | -5.5% | $510.37 | -1.7 | done | can't tell from luck |
| value_ev10 | 727 | 37.3 | 39.3 | $-712.65 | -9.8% | $287.35 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 1560 | 49.3 | 49.8 | $-842.34 | -5.4% | $157.66 | -2.1 | done | losing for real |
| value_ev5 | 1081 | 39.7 | 41.2 | $-860.10 | -8.0% | $139.90 | -2.2 | done | losing for real |
| reversal_15m_0.10pct | 1560 | 50.7 | 51.1 | $-888.22 | -5.7% | $111.78 | -2.3 | done | losing for real |
| coinflip | 2208 | 50.0 | 50.5 | $-1234.36 | -5.6% | $-234.36 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 1307 | 48.7 | 51.2 | $-1305.58 | -10.0% | $-305.58 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2208 | 50.3 | 51.8 | $-1540.84 | -7.0% | $-540.84 | -3.4 | done | losing for real |
| always_up | 2208 | 46.8 | 49.9 | $-2365.99 | -10.7% | $-1365.99 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3473 | 47.5 | 49.2 | $-2803.65 |
| ETH | 3827 | 47.9 | 48.6 | $-2711.61 |
| SOL | 4007 | 47.8 | 48.7 | $-3004.59 |
| XRP | 4052 | 48.5 | 48.6 | $-2263.91 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
