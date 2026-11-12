# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 9:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 113 windows, 2893 settled trades, 52 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 222 | 61.3 | 53.0 | $+297.46 | +13.4% | $1297.46 | +2.1 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 279 | 55.6 | 52.1 | $+129.66 | +4.6% | $1129.66 | +0.8 | done | can't tell from luck |
| momentum_5m_0.00pct | 444 | 52.5 | 50.6 | $-0.16 | -0.0% | $999.84 | -0.0 | done | can't tell from luck |
| value_ev10 | 148 | 40.5 | 40.7 | $-70.13 | -4.7% | $929.87 | -0.5 | Thu 8:15 AM | too few trades (148/200) |
| value_ev20 | 50 | 28.0 | 36.5 | $-123.85 | -24.8% | $876.15 | -1.4 | Sun 4:15 PM | too few trades (50/200) |
| value_ev5 | 207 | 38.2 | 42.0 | $-259.73 | -12.5% | $740.27 | -1.6 | done | can't tell from luck |
| coinflip | 444 | 50.2 | 51.4 | $-262.58 | -5.9% | $737.42 | -1.3 | done | can't tell from luck |
| trend_filter | 154 | 40.9 | 48.8 | $-287.88 | -18.7% | $712.12 | -2.3 | Thu 6:45 AM | too few trades (154/200) |
| momentum_15m_0.10pct | 279 | 44.4 | 50.1 | $-389.39 | -14.0% | $610.61 | -2.4 | done | losing for real |
| always_up | 444 | 46.6 | 50.4 | $-485.63 | -10.9% | $514.37 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 222 | 38.7 | 49.1 | $-508.89 | -22.9% | $491.11 | -3.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 624 | 45.8 | 49.8 | $-561.68 |
| ETH | 705 | 45.8 | 49.0 | $-658.39 |
| SOL | 773 | 48.3 | 48.6 | $-520.99 |
| XRP | 791 | 50.3 | 49.1 | $-220.07 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
