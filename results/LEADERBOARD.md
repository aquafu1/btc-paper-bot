# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 6:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 425 windows, 11685 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 210 | 34.8 | 36.4 | $-166.95 | -8.0% | $833.05 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 999 | 50.5 | 50.0 | $-336.33 | -3.4% | $663.67 | -1.1 | done | can't tell from luck |
| value_ev10 | 545 | 39.3 | 40.4 | $-345.95 | -6.3% | $654.05 | -1.2 | done | can't tell from luck |
| trend_filter | 668 | 49.4 | 50.7 | $-448.88 | -6.7% | $551.12 | -1.8 | done | can't tell from luck |
| value_ev5 | 819 | 41.3 | 42.1 | $-473.19 | -5.8% | $526.81 | -1.4 | done | can't tell from luck |
| momentum_15m_0.10pct | 1183 | 49.0 | 50.0 | $-656.00 | -5.5% | $344.00 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1183 | 51.0 | 51.8 | $-679.18 | -5.7% | $320.82 | -2.1 | done | losing for real |
| coinflip | 1693 | 50.6 | 51.0 | $-757.47 | -4.5% | $242.53 | -1.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 999 | 49.5 | 51.9 | $-856.15 | -8.6% | $143.85 | -2.8 | done | losing for real |
| momentum_5m_0.00pct | 1693 | 49.5 | 51.6 | $-1292.00 | -7.6% | $-292.00 | -3.3 | done | losing for real |
| always_up | 1693 | 46.1 | 50.6 | $-2136.60 | -12.6% | $-1136.60 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2645 | 47.6 | 49.4 | $-1976.13 |
| ETH | 2929 | 48.0 | 49.0 | $-1857.42 |
| SOL | 3028 | 47.7 | 49.5 | $-2579.96 |
| XRP | 3083 | 48.8 | 49.3 | $-1735.20 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
