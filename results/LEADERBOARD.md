# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 10:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 731 windows, 20119 settled trades, 64 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 381 | 33.3 | 34.9 | $-334.03 | -8.8% | $665.97 | -1.3 | done | can't tell from luck |
| reversal_15m_0.10pct | 2062 | 51.6 | 50.7 | $-457.55 | -2.2% | $542.45 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 1688 | 50.2 | 49.6 | $-537.77 | -3.2% | $462.23 | -1.3 | done | can't tell from luck |
| value_ev10 | 920 | 38.0 | 39.1 | $-595.30 | -6.5% | $404.70 | -1.6 | done | can't tell from luck |
| value_ev5 | 1390 | 40.6 | 41.1 | $-710.36 | -5.1% | $289.64 | -1.6 | done | can't tell from luck |
| trend_filter | 1180 | 50.1 | 51.0 | $-719.54 | -6.1% | $280.46 | -2.1 | done | losing for real |
| coinflip | 2916 | 50.3 | 50.3 | $-1201.31 | -4.1% | $-201.31 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 1688 | 49.8 | 51.2 | $-1258.54 | -7.5% | $-258.54 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 2062 | 48.4 | 50.1 | $-1492.61 | -7.2% | $-492.61 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 2916 | 50.8 | 51.8 | $-1628.42 | -5.6% | $-628.42 | -3.1 | done | losing for real |
| always_up | 2916 | 47.0 | 49.6 | $-2705.04 | -9.3% | $-1705.04 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4555 | 48.1 | 49.1 | $-2867.76 |
| ETH | 5013 | 48.1 | 48.5 | $-3086.91 |
| SOL | 5239 | 48.1 | 48.7 | $-3088.46 |
| XRP | 5312 | 48.5 | 48.5 | $-2597.32 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
