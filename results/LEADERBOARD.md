# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 8:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 771 windows, 21257 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 402 | 33.1 | 34.9 | $-371.45 | -9.2% | $628.55 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 2169 | 51.4 | 50.6 | $-582.29 | -2.7% | $417.71 | -1.3 | done | can't tell from luck |
| value_ev10 | 974 | 37.7 | 39.1 | $-694.62 | -7.1% | $305.38 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1798 | 49.8 | 49.6 | $-770.69 | -4.3% | $229.31 | -1.8 | done | can't tell from luck |
| trend_filter | 1247 | 49.6 | 50.8 | $-855.43 | -6.9% | $144.57 | -2.5 | done | losing for real |
| value_ev5 | 1472 | 40.0 | 41.0 | $-894.74 | -6.1% | $105.26 | -2.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 1798 | 50.2 | 51.2 | $-1166.18 | -6.5% | $-166.18 | -2.8 | done | losing for real |
| coinflip | 3076 | 50.3 | 50.3 | $-1243.75 | -4.0% | $-243.75 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 2169 | 48.6 | 50.2 | $-1490.31 | -6.9% | $-490.31 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 3076 | 50.9 | 51.6 | $-1562.34 | -5.1% | $-562.34 | -2.9 | done | losing for real |
| always_up | 3076 | 47.1 | 49.6 | $-2775.64 | -9.0% | $-1775.64 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4825 | 48.2 | 49.1 | $-2887.24 |
| ETH | 5306 | 47.9 | 48.5 | $-3575.00 |
| SOL | 5531 | 48.0 | 48.5 | $-3227.92 |
| XRP | 5595 | 48.5 | 48.4 | $-2717.28 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
