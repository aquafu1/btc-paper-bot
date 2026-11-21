# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 12:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1026 windows, 28567 settled trades, 44 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 530 | 34.7 | 35.1 | $-278.51 | -5.3% | $721.49 | -0.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2909 | 51.1 | 50.5 | $-879.86 | -3.0% | $120.14 | -1.6 | done | can't tell from luck |
| value_ev10 | 1313 | 37.5 | 39.2 | $-977.78 | -7.4% | $22.22 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2459 | 49.9 | 49.6 | $-1062.65 | -4.3% | $-62.65 | -2.1 | done | losing for real |
| trend_filter | 1712 | 49.5 | 50.7 | $-1251.06 | -7.3% | $-251.06 | -3.1 | done | losing for real |
| value_ev5 | 1988 | 39.4 | 41.0 | $-1417.33 | -7.1% | $-417.33 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2459 | 50.1 | 51.0 | $-1647.90 | -6.7% | $-647.90 | -3.4 | done | losing for real |
| coinflip | 4096 | 50.5 | 50.4 | $-1698.85 | -4.1% | $-698.85 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 2909 | 48.9 | 50.3 | $-1944.53 | -6.7% | $-944.53 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 4096 | 50.7 | 51.5 | $-2264.00 | -5.5% | $-1264.00 | -3.7 | done | losing for real |
| always_up | 4096 | 47.4 | 49.5 | $-3597.26 | -8.8% | $-2597.26 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6513 | 48.3 | 49.1 | $-3523.89 |
| ETH | 7093 | 48.1 | 48.5 | $-4393.01 |
| SOL | 7459 | 48.2 | 48.6 | $-4289.90 |
| XRP | 7502 | 48.1 | 48.4 | $-4812.93 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
